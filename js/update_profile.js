// Åbn - luk pop up 
function open_edit_profile() {
    const edit_profile_pop_up = document.getElementById("edit_profile_pop_up")
    const close_edit_profile_pop_up = document.getElementById("close_edit_profile_pop_up")

    // Open close
    if(edit_profile_pop_up.classList.contains("hidden")) {
        edit_profile_pop_up.classList.remove("hidden")
        edit_profile_pop_up.classList.add("flex")
    } else {
        edit_profile_pop_up.classList.add("hidden")
        edit_profile_pop_up.classList.remove("flex")
    }
}


// Luk pop up, hvis brugeren klikker på baggrunds div / overlay
function close_edit_profile(event) {
  const edit_profile_form = document.getElementById("edit_profile_form")
  const target = event.target

  // Check if the target is outside the edit profile form
  if (!edit_profile_form.contains(target)) {
    const edit_profile_pop_up = document.getElementById("edit_profile_pop_up")
    edit_profile_pop_up.classList.add("hidden")
    edit_profile_pop_up.classList.remove("flex")
  }
}



// DOMContentLoaded = a specific event name recognized by browsers to indicate that the initial HTML document has finished loading
document.addEventListener("DOMContentLoaded", function() {
  const close_edit_profile_pop_up = document.getElementById("close_edit_profile_pop_up")
  const edit_profile_pop_up = document.getElementById("edit_profile_pop_up")

  close_edit_profile_pop_up.addEventListener("click", open_edit_profile)
  edit_profile_pop_up.addEventListener("click", close_edit_profile)
})




async function update_profile() {
  const frm = event.target

  const conn = await fetch("/profile", {
    method : "PUT",
    body : new FormData(frm)
  })
  const data = await conn.json()

  if(conn.ok && data.info == "ok") {
    location.reload(); // Reload the page
    console.log("der er forbindelse")
  } else {
    const update_user_error_message = document.getElementById("update_user_error_message")
    update_user_error_message.innerHTML = "Cannot update your profile, try again later"
    console.log("Cannot update profile")
  }

}


