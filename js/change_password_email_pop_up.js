
// Åbn - luk pop up 
function open_change_password_pop_up() {
    const change_password_pop_up = document.getElementById("change_password_pop_up")
    // Open close
    if(change_password_pop_up.classList.contains("hidden")) {
        change_password_pop_up.classList.remove("hidden")
        change_password_pop_up.classList.add("flex")  
        console.log("open")
    } else {
        change_password_pop_up.classList.add("hidden")
        change_password_pop_up.classList.remove("flex")
        console.log("close")
    }
}
// Luk ved klik uden for kassen
function close_change_password_pop_up(event) {
    const change_password_form = document.getElementById("change_password_form")
    const target = event.target

  // Check if the target is outside the edit profile form
  if (!change_password_form.contains(target)) {
    const change_password_pop_up = document.getElementById("change_password_pop_up")
    change_password_pop_up.classList.add("hidden")
    change_password_pop_up.classList.remove("flex")
  }
}
// Event listeners
// DOMContentLoaded = a specific event name recognized by browsers to indicate that the initial HTML document has finished loading
document.addEventListener("DOMContentLoaded", function() {
  const x_change_password_pop_up = document.getElementById("x_change_password_pop_up")
  const change_password_pop_up = document.getElementById("change_password_pop_up")

  x_change_password_pop_up.addEventListener("click", open_change_password_pop_up)
  change_password_pop_up.addEventListener("click", close_change_password_pop_up)
})


async function change_password_submit(){
    const frm = event.target
    const conn = await fetch("/change-password-submit", {
        method: "POST",
        body: new FormData(frm)
    })
    const data = await conn.json()

    if( conn.ok && data.info == "ok" ) {
        console.log("nice")
        open_change_password_pop_up()
    } else {
        const chanage_password_error_message = document.getElementById("chanage_password_error_message")
        chanage_password_error_message.innerHTML = "Cannot send email to change password"
    }
}

