<template>
    <v-card>
        <v-layout>
            <v-navigation-drawer v-model="drawer" :rail="rail" permanent>
                <v-list-item @click="test" prepend-icon="mdi-menu" value="menu" nav @click.stop="rail = !rail">
                    <v-img id="QuantoLogo" src="../icons/QuantoLogo.svg" @click.stop></v-img>
                </v-list-item>

                <v-divider></v-divider>

                <v-list density="compact" nav>
                    <v-list-item prepend-icon="mdi-home" title="Home" value="home">
                    </v-list-item>
                    <v-list-item prepend-icon="mdi-account-clock-outline" title="Working Times+"
                        value="workingTimes+"></v-list-item>
                    <v-list-item prepend-icon="mdi-cog-outline" title="Settings" value="settings"></v-list-item>
                    <v-list-item prepend-icon="mdi-plus-circle-outline" title="New Project" value="project"></v-list-item>
                    <v-list-item prepend-icon="mdi-account-cog-outline" title="Manage Project"
                        value="manageProject"></v-list-item>
                    <v-list-item prepend-icon="mdi-timer-sand" title="Time Registration"
                        value="timeRegistration"></v-list-item>

                    <div class="logoutContainer">
                        <v-list-item class="Profil" prepend-avatar="../icons/Test.jpg" title="Chris Schröder"
                            value="Profil"></v-list-item>
                        <v-list-item id="logoutIcon" class="logoutBtn" prepend-icon="mdi-logout" title="Logout"
                            value="logout">
                        </v-list-item>
                    </div>
                </v-list>
            </v-navigation-drawer>
            <v-main></v-main>
        </v-layout>
    </v-card>
</template>

<style scoped>
#QuantoLogo {
    cursor: default;
}

.logoutContainer {
    margin-top: 300px;
}

.v-navigation-drawer {
    background-color: #94B8C7;
}
</style>

<style>
.logoutBtn {
    background-color: white !important;
}

.logoutBtn .v-list-item-title {
    color: black !important;
}

.v-list-item-title {
    color: white;
}
</style>


<script>
export default {
    data() {
        return {
            drawer: true,
            rail: true,
        }
    },

}
</script>

<script setup>
function test() {

}
</script>