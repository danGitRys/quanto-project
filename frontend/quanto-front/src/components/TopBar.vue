<template>
    <header>
        <div class="arrowIconContainer">
            <img src="../icons/Arrow.png" alt="arrowIconLeft" id="arrowIconLeft">
            <img src="../icons/Arrow.png" alt="arrowIconRight" id="arrowIconRight">
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
                if (!User.isLoggedIn) {
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
    display: flex;
    justify-content: end;
    align-items: center;
    box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
    position: sticky;
}

#arrowIconRight {
    margin-left: 30px;
    transform: rotate(180deg);
    cursor: pointer;
}

.arrowIconContainer {
    margin-right: 50px;
    cursor: pointer;
}
</style>

