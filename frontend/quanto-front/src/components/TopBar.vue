<template>
    <header>
        <div class="headerContainer">
            <div class="headerDiv">{{ $route.name }}</div>
            <div class="quantoLogoImage"></div>
            <Button label="Logout" @click="logoutDialog"/>
        </div>
    </header>
    <Dialog v-model:visible="logoutDialogVisible" :style="{width: '450px'}" header="Confirm" :modal="true">
        <div class="confirmation-content">
            <i class="pi pi-exclamation-triangle mr-3" style="font-size: 2rem" />
            <span>Are you sure you want to log out?</span>
        </div>
        <template #footer>
            <Button label="No" icon="pi pi-times" text @click="closeDialog"/>
            <Button label="Yes" icon="pi pi-check" text @click="logout" />
        </template>
    </Dialog>
</template>

<script>
import Dialog from 'primevue/dialog'
import { useUser } from '@/store/user';

export default {
    name: "TopBar",
    components: {
        Dialog,
    },
    data() {
        return {
            logoutDialogVisible: false,
            User: useUser(),

            // Event Handler
            logoutDialog: () => {
                const User = useUser()
                if (User.isLoggedIn) {
                    this.logoutDialogVisible = true
                }
            },
            closeDialog: () => {
                this.logoutDialogVisible = false
            },
            logout: () => {
                const User = useUser()
                this.logoutDialogVisible = false
                User.logoutUser()
                window.location.href = '/';
            },
        }
    },
    methods: {
        
    }
}

</script>

<style scoped>
header {
    top: 0px;
    height: 110px;
    background-color: #94B8C7;
    box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
    position: sticky;
}

.headerContainer {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0 40px;
}

.headerDiv {
    font-size: 32px;
    font-weight: 600;
    text-align: center;
    flex:1;
    margin-left:250px ;
   
}

.quantoLogoImage {
    background: url('../icons/QuantoLogo.svg') no-repeat center;
    width: 250px;
    height: 100px;
}
</style>
