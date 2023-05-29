// Definer globale variabler
let active_profile_pop_up = null;
let profile_options_btn_g 
let profile_options_btn

/**
 * Denne funktion bliver kaldt en gang når js filen bliver importeret
 * - Formålet med dette er at lave kun en eventlistener.
 */
function initialize() {
    // Luk popup når user klikker udenfor knap, popup eller på andre knapper
    document.addEventListener("click", (e) => {
         if (active_profile_pop_up && e.target !== active_profile_pop_up.button && !active_profile_pop_up.popup.contains(e.target)  && !active_profile_pop_up.button.contains(e.target)) {
            console.log(e.target);
            active_profile_pop_up.popup.classList.remove("flex");
            active_profile_pop_up.popup.classList.add("hidden");
            active_profile_pop_up = null;
        } 
    });
}

// Kald når js filen bliver importeret
initialize();

/**
 * Åbn & Luk pop up til logud i navbar
 * @param {HTMLElement} profile_options_btn - Inderholder profil muligheder knappen.
 */
function open_profile_option_btn(profile_options_btn) {
    profile_options_btn_g = profile_options_btn
    let profile_option_popup = document.getElementById("profile_option_popup")    

    // Hvis eller skjul popup
    if (active_profile_pop_up && active_profile_pop_up.popup !== profile_option_popup) {
        active_profile_pop_up.popup.classList.remove("flex");
        active_profile_pop_up.popup.classList.add("hidden");
        active_profile_pop_up = null;
    }

    // Skjul pop up
    if(profile_option_popup.classList.contains("flex")) {
        profile_option_popup.classList.add("hidden")
        profile_option_popup.classList.remove("flex")
        active_profile_pop_up = null;
    // Åbn pop up
    } else { 
        profile_option_popup.classList.add("flex")
        profile_option_popup.classList.remove("hidden")
        active_profile_pop_up = { button: profile_options_btn, popup: profile_option_popup };
    }
}

