<template>
    <div class="topBar">
        <div class="arrowIconContainer">
                <img src="../icons/Arrow.png" alt="arrowIconLeft" id="arrowIconLeft">
                <img src="../icons/Arrow.png" alt="arrowIconRight" id="arrowIconRight">
        </div>
    </div>
</template>
<style scoped>
.topBar{
    height: 110px;
    background-color: #94B8C7;
    display: flex;
    justify-content: end;
    align-items: center;
    box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
}
#arrowIconRight{
    margin-left: 30px;
    transform: rotate(180deg);
    cursor: pointer;
}
.arrowIconContainer{
margin-right: 50px;
cursor: pointer;
}
</style>

