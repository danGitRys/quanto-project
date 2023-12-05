<template>
    <footer>
        <button class="create-button" @click="createProject">Create</button>
    </footer>
</template>

<script>
</script>

<style scoped>
footer {
    position: sticky;
    bottom: 0px;
    width: 100%;
    height: 75px;
    background-color: #94B8C7;
    display: flex;
    justify-content: end;
    align-items: center;
    box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
}

.create-button {
  background-color: orange;
  /* Blaue Hintergrundfarbe */
  color: white;
  border: none;
  border-radius: 5px;
  padding: 10px 20px;
  cursor: pointer;
  margin-top: 10px;
  font-size: 18px;
  transition: background-color 0.3s;
  display: block;
  /* Ändern Sie die Anzeige auf "block" */
  margin: 10px auto;
  /* Auto-Margin horizontal zentriert den Button */
}

.create-button:hover {
  background-color: #0056b3;
  /* Farbänderung bei Hover */
}
</style>