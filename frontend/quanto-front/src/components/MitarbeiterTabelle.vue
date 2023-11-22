<template>
    <div class="container">
        <div class="card p-fluid">
            <DataTable :value="products" editMode="cell" @cell-edit-complete="onCellEditComplete" :pt="{
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
                        <span v-else>{{ field === 'price' ? formatCurrency(data[field]) : data[field] }}</span>
                    </template>
                    <template #editor="{ data, field }">
                        <template v-if="field !== 'price'">
                            <InputText v-model="data[field]" ref="inputField" @input="onInput" />
                        </template>
                        <template v-else>
                            <InputNumber v-model="data[field]" mode="currency" currency="USD" locale="en-US"
                                ref="inputField" @input="onInput" />
                        </template>
                    </template>
                </Column>
            </DataTable>
        </div>
    </div>
</template>

<script>
import { ProductService } from '@/service/ProductService';
import InputText from 'primevue/inputtext';
import InputNumber from 'primevue/inputnumber'; // Import der InputNumber-Komponente

export default {
    components: {
        InputText,
        InputNumber // Registrieren Sie die InputNumber-Komponente
    },
    data() {
        return {
            products: null,
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
        ProductService.getProductsMini().then((data) => {
            this.products = data;
        });
    },
    methods: {
        onCellEditComplete: function (event) {
            let { data, newValue, field } = event;

            switch (field) {
                case 'quantity':
                case 'price':
                    if (this.isPositiveInteger(newValue)) data[field] = newValue;
                    else event.preventDefault();
                    break;

                default:
                    if (newValue.trim().length > 0) data[field] = newValue;
                    else event.preventDefault();
                    break;
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
        formatCurrency(value) {
            return new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD' }).format(value);
        },
        onInput() {
            if (this.$refs.inputField && this.$refs.inputField.$props) {
                this.editingRow = this.$refs.inputField.$props.value;
            }
        }
    }
};
</script>

<style scoped>
.container {
    position: relative;
    /* Füge Positionierung hinzu */
}

.p-datatable {
    position: absolute;
    /* Ändere die Position auf absolute */
    bottom: 35em;
    /* Ändere die Position auf den oberen Rand des .container-Elements */
    left: 6em;
    /* Ändere die Position auf den linken Rand des .container-Elements */
}
</style>
