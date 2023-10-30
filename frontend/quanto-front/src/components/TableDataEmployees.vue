<template>
    <h2>Projekt 1</h2>
    <div>
        <h3 @click="toggleTable">
            {{ isTableOpen ? '➖' : '➕' }} Mitarbeiter: Hans Zimmer
        </h3>
        <v-table v-if="isTableOpen">
            <thead>
                <tr>
                    <th class="text-left">Datum</th>
                    <th class="text-left">Projekt1</th>
                    <th class="text-left">Projekt2</th>
                    <th class="text-left">Projekt3</th>
                    <th class="text-left">Summe</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="item in infoData" :key="item.datum">
                    <td>{{ item.datum }}</td>
                    <td>{{ item.project1 }}</td>
                    <td>{{ item.project2 }}</td>
                    <td>{{ item.project3 }}</td>
                    <td>{{ item.summe }}</td>
                </tr>
            </tbody>
        </v-table>
    </div>

    <div>
        <h3 @click="toggleTable2">
            {{ isTableOpen2 ? '➖' : '➕' }} Mitarbeiter: Bernd Müller
        </h3>
        <v-table v-if="isTableOpen2">
            <thead>
                <tr>
                    <th class="text-left">Datum</th>
                    <th class="text-left">Projekt1</th>
                    <th class="text-left">Projekt2</th>
                    <th class="text-left">Projekt3</th>
                    <th class="text-left">Summe</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="item in infoData" :key="item.datum">
                    <td>{{ item.datum }}</td>
                    <td>{{ item.project1 }}</td>
                    <td>{{ item.project2 }}</td>
                    <td>{{ item.project3 }}</td>
                    <td>{{ item.summe }}</td>
                </tr>
            </tbody>
        </v-table>
    </div>
</template>

<style>
th {
    border: 1px solid black;
}

td {
    border: 1px solid black;
}
</style>

<script>
export default {
    data() {
        return {
            isTableOpen: false,
            isTableOpen2: false,
            infoData: [
                {
                    datum: 'So, 01.10.2023',
                    project1: 0,
                    project2: 8,
                    project3: 0,
                    summe: 8,
                },
                {
                    datum: 'Mo, 02.10.2023',
                    project1: 4,
                    project2: 4,
                    project3: 0,
                    summe: 8,
                },
                {
                    datum: 'Di, 03.10.2023',
                    project1: 6,
                    project2: 0,
                    project3: 2,
                    summe: 8,
                },
                {
                    datum: 'Mi, 04.10.2023',
                    project1: 8,
                    project2: 0,
                    project3: 0,
                    summe: 8,
                },
                {
                    datum: 'Do, 05.10.2023',
                    project1: 0,
                    project2: 0,
                    project3: 8,
                    summe: 8,
                },
                {
                    datum: 'Fr, 06.10.2023',
                    project1: 2,
                    project2: 2,
                    project3: 4,
                    summe: 8,
                },
                {
                    datum: 'Sa, 07.10.2023',
                    project1: 3,
                    project2: 4,
                    project3: 1,
                    summe: 8,
                },
            ],
        }
    },
    methods: {
        toggleTable() {
            this.isTableOpen = !this.isTableOpen
        },
        toggleTable2() {
            this.isTableOpen2 = !this.isTableOpen2
        },
    },
}
</script>
