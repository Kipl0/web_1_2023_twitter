/**
 * Updater profil, forbindelse til api
 */
async function update_profile() { 
  try {    
    // Hent event target som i vores tilfælde er en form
    const frm = event.target

    // Lav reqeust til vores API om at opdatere profil
    const conn = await fetch("/profile", {
      method : "PUT",
      body : new FormData(frm)
    })

    // Hent response fra API
    const data = await conn.json()

    // Tjek om requestet gik igennem og kast en error hvis ikke det skete
    if( !conn.ok || data.info != "ok" ) {
      const update_user_error_message = document.getElementById("update_user_error_message")
      update_user_error_message.innerHTML = "Cannot update your profile, try again later"
      throw new TypeError("Something went wrong");
    }

    // Reload siden
    location.reload(); 
  } 
  catch ({ name, message }) {
      console.log(name); 
      console.log(message); 
  }
}

// function show_confirm_button() {
//     const show_confirm_buttons = document.getElementById("show_confirm_buttons")
//     const deactivate_profile_btn = document.getElementById("deactivate_profile_btn")

//     // dobbelttjek her er nødvendigt i tilfælde af at bruger har klikker på cancel
//     if (show_confirm_buttons.classList.contains("hidden")) {
//       show_confirm_buttons.classList.remove("hidden")
//       show_confirm_buttons.classList.add("flex")

//       deactivate_profile_btn.classList.remove("flex")
//       deactivate_profile_btn.classList.add("hidden")

//     } else {
//       show_confirm_buttons.classList.add("hidden")
//       show_confirm_buttons.classList.remove("flex")

//       deactivate_profile_btn.classList.add("flex")
//       deactivate_profile_btn.classList.remove("hidden")
//     }
// }


/**
 * Åbn & Luk edit profil pop up 
 */
function open_edit_profile() {
  const edit_profile_pop_up = document.getElementById("edit_profile_pop_up")
  // Open close
  if(edit_profile_pop_up.classList.contains("hidden")) {
      edit_profile_pop_up.classList.remove("hidden")
      edit_profile_pop_up.classList.add("flex")
  } else {
      edit_profile_pop_up.classList.add("hidden")
      edit_profile_pop_up.classList.remove("flex")
  }
}

/**
 * Luk pop up, hvis brugeren klikker på baggrunds div / overlay
 * @param {Event} event - event.
 */
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


/**
 * Denne funktion bliver kaldt en gang når js filen bliver importeret
 * - Formålet med dette er at lave kun en eventlistener.
 */
function init() {
  // DOMContentLoaded = a specific event name recognized by browsers to indicate that the initial HTML document has finished loading
  document.addEventListener("DOMContentLoaded", function() {
    const close_edit_profile_pop_up = document.getElementById("close_edit_profile_pop_up")
    const edit_profile_pop_up = document.getElementById("edit_profile_pop_up")

    close_edit_profile_pop_up.addEventListener("click", open_edit_profile)
    edit_profile_pop_up.addEventListener("click", close_edit_profile)
  })

  // Hvis billederne i deres kasse, når der er valgt et nyt billede
  let uploaded_avatar = "";
  const uploaded_avatar_input = document.getElementById("uploaded_avatar_input");

  uploaded_avatar_input.addEventListener("change", function() {
    const reader = new FileReader();
    reader.addEventListener("load", () => {
      uploaded_avatar = reader.result;
      document.getElementById("uploaded_avatar").src = uploaded_avatar;
    });
    reader.readAsDataURL(this.files[0]);
  });

  let uploaded_banner = "";
  const uploaded_banner_input = document.getElementById("uploaded_banner_input");

  uploaded_banner_input.addEventListener("change", function() {
    const reader = new FileReader();
    reader.addEventListener("load", () => {
      uploaded_banner = reader.result;
      document.getElementById("uploaded_banner").src = uploaded_banner;
    });
    reader.readAsDataURL(this.files[0]);
  });

  // document.getElementById("imageid").src="../template/save.png";
}

// Kald når js filen bliver importeret
init();






