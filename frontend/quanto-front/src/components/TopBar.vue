

<template>
    <div class="topBar">
        <div class="arrowIconContainer">
                <img src="../icons/Arrow.png" alt="arrowIconLeft" id="arrowIconLeft">
                <img src="../icons/Arrow.png" alt="arrowIconRight" id="arrowIconRight">
        </div>
    </div>
</template>
<style >
.topBar{
    height: 110px;
    background-color: blueviolet;
    display: flex;
    justify-content: end;
    align-items: center;

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

