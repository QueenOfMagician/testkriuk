let box2Open = false;
const toggleButton = document.getElementById("toggleButton");
const arrowImage = document.querySelector(".arrow-image");

function toggleBox2() {
  const box2 = document.getElementById("box2");

  if (!box2Open) {
    box2.style.flex = "0 0 400px";
    arrowImage.src = "{% static 'img/kanan.png' %}";
  } else {
    box2.style.width = "0";
    box2.style.flex = 0;
    arrowImage.src = "{% static 'img/kiri.png' %}";
  }
  box2Open = !box2Open;
}
function openBox2() {
  if (box2Open) {
    toggleBox2();
  }
}
