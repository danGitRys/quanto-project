<template>
    <div class="container">
        <div class="card p-fluid">
            <DataTable :value="displayedData" editMode="cell" @cell-edit-complete="onCellEditComplete" :pt="{
                table: { style: 'min-width: 50rem' },
                column: {
                    bodycell: ({ state }) => ({
                        class: [{ 'pt-0 pb-0': state['d_editing'] }]
                    })
                }
            }">
                <Column v-for="col of columns" :key="col.field" :field="col.field" :header="col.header" style="width: 25%">
                    <template #body="{ data, field }">
                        <span v-if="editingRow === data">Editing...</span>
                        <span v-else>
                            {{ field === 'date' ? formatDate(data[field]) : data[field] }}
                        </span>
                    </template>

                    <template v-if="col.field !== 'date'" #editor="{ data, field }">
                        <InputText v-model="data[field]" ref="inputField" @input="onInput" />
                    </template>
                </Column>
            </DataTable>
        </div>
    </div>
</template>

<script>
import InputText from 'primevue/inputtext';

export default {
    components: {
        InputText
    },
    data() {
        return {
            generatedDate: [],
            columns: [
                { field: 'date', header: 'Date' },
                { field: 'hours_in_projects', header: 'Hours in Projects' },
                { field: 'hours_this_project', header: 'Hours this Project' },
                { field: 'pos', header: 'Pos' }
            ],
            editingRow: null
        };
    },
    mounted() {
        this.generateDatesForCurrentMonth();
    },
    computed: {
        displayedData() {
            return [...this.generatedDate];
        }
    },
    methods: {
        onCellEditComplete: function (event) {
            let { data, newValue, field } = event;

            if (data[field] !== newValue) {
                switch (field) {
                    case 'hours_in_projects':
                    case 'hours_this_project':
                        if (typeof newValue === 'string' && this.isPositiveInteger(newValue.trim())) {
                            data[field] = newValue.trim();
                        } else {
                            event.preventDefault();
                        }
                        break;

                    default:
                        if (typeof newValue === 'string' && newValue.trim().length > 0) {
                            data[field] = newValue.trim();
                        } else {
                            event.preventDefault();
                        }
                        break;
                }

                this.editingRow = null;
            }
        },

        isPositiveInteger(val) {
            let str = String(val);
            str = str.trim();
            if (!str) {
                return false;
            }
            str = str.replace(/^0+/, '') || '0';
            var n = Math.floor(Number(str));
            return n !== Infinity && String(n) === str && n >= 0;
        },

        onInput() {
            const inputFieldValue = this.$refs.inputField?.$props?.value;
            this.editingRow = inputFieldValue;
        },

        daysInMonth(month, year) {
            return new Date(year, month, 0).getDate();
        },

        generateDatesForCurrentMonth() {
            let date = new Date();
            let month = date.getMonth() + 1;
            let year = date.getFullYear();
            let daysInMonth = this.daysInMonth(month, year);

            let dateOnlyNumbers = `${year}-${month < 10 ? '0' : ''}${month}-${daysInMonth < 10 ? '0' : ''}${daysInMonth}`;
            console.log(dateOnlyNumbers);

            for (let day = 1; day <= daysInMonth; day++) {
                this.generatedDate.push({
                    date: new Date(year, month - 1, day),
                });
            }
        },

        formatDate(date) {
            const options = { weekday: 'short', day: 'numeric', month: 'short', year: 'numeric' };
            return new Intl.DateTimeFormat('en-US', options).format(date);
        }
    }
};
</script>

<style scoped>
.container {
    position: relative;
}

.card {
    position: absolute;
    bottom: -6em;
    left: 6em;
}
</style>
