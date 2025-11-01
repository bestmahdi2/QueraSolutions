const edit = document.querySelectorAll(".edit-icon");
const port_number = document.querySelectorAll(".port-number");
let btn = document.querySelectorAll(".save-button");
let edit_input = document.querySelectorAll(".edit-input");
const newval = [];
for (let i = 0; i < 5; i++) {
  edit[i].addEventListener("click", () => {
    const container = edit[i].parentElement;
    if (
      container.querySelector("input.edit-input") ||
      container.querySelector("button.save-button")
    ) {
      return;
    }

    const val = port_number[i].innerHTML;
    port_number[i].innerHTML = "";
    const input = document.createElement("input");
    input.type = "number";
    input.value = val;
    input.classList.add("edit-input");

    const submitBtn = document.createElement("button");
    submitBtn.textContent = "ثبت";
    submitBtn.classList.add("save-button");

    container.appendChild(input);
    container.appendChild(submitBtn);
    submitBtn.addEventListener("click", () => {
      port_number[i].innerHTML = input.value;
      if (input.value == "") {
        port_number[i].innerHTML = val;
      }
      input.style.display = "none";
      submitBtn.style.display = "none";
    });
  });
}
