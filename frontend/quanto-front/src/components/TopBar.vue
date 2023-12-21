<template>
    <header>
        <div class="headerContainer">
            <div class="headerDiv">{{ $route.name }}</div>
            <div class="quantoLogoImage"></div>
        </div>
    </header>
</template>

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
