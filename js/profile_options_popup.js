
// åbn og luk pop up til logud i ... navbar

function open_profile_option_btn() {
    let profile_option_popup = document.getElementById("profile_option_popup")    

    // close it
    if(profile_option_popup.classList.contains("flex")) {
        profile_option_popup.classList.add("hidden")
        profile_option_popup.classList.remove("flex")
    } else { // open
        profile_option_popup.classList.add("flex")
        profile_option_popup.classList.remove("hidden")
    }


}