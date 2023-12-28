<template>
    <div>
        <table>
            <thead>
                <tr>
                    <th>Name</th>
                    <th>Alter</th>
                    <th>Stadt</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <!-- Verwende den ausgewählten Index, um das entsprechende Element auszuwählen -->
                    <td>{{ people[selectedPersonIndex].name }}</td>
                    <td>{{ people[selectedPersonIndex].age }}</td>
                    <td>{{ people[selectedPersonIndex].city }}</td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script setup>
import { defineProps } from 'vue';

const { people, selectedPersonIndex } = defineProps(['people', 'selectedPersonIndex']);
</script>
