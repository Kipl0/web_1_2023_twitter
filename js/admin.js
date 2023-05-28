/**
 * Lav et request til vores api om at deaktivere brugeren
 */
async function deactivate_user() {
    try {
        // Hent event target som i vores tilfælde er en form
        const frm = event.target.form

        // Lav reqeust til vores API om at deactivate-user
        const conn = await fetch("/deactivate-user", {
            method : "POST",
            body : new FormData(frm),        
        })

        // Hent response fra API
        const data = await conn.json()

        // Tjek om requestet var succesfuldt
        if( !conn.ok || data.info != "ok" ) {
            throw new TypeError("Something went wrong. Cannot write comment to tweet");
        }
    
        // Reload side 
        location.reload()
    } 
    catch ({ name, message }) {
        console.log(name); 
        console.log(message); 
    }
}
/**
 * Hvis confirmer knappen
 * @param {HTMLElement} delete_user_button - button that is pressed
 */
function show_confirm_button(delete_user_button) {


    const tweet_option_popup_text = "show_confirm_buttons_admin_"
    
    // Split the text from the id where _
    const parts = delete_user_button.id.split("_");
    const id = parts[parts.length - 1];
    const show_confirm_buttons = document.getElementById(tweet_option_popup_text + id)
    
    // Opdater styling
    show_confirm_buttons.classList.remove("hidden")
    show_confirm_buttons.classList.add("flex")
    
    delete_user_button.classList.remove("flex")
    delete_user_button.classList.add("hidden")
}

/**
 * Hvis confirmer knappen
* @param {HTMLElement} button - button that is pressed
 */
function hide_confirm_button(button) {
    const show_confirm_buttons_admin = "show_confirm_buttons_admin_"
    const delete_user_button = "delete_user_button_"

    // Split the text from the id where _
    const parts = button.id.split("_");
    const id = parts[parts.length - 1];

    const show_confirm_buttons_admin_element = document.getElementById(show_confirm_buttons_admin + id)
    const delete_user_button_element = document.getElementById(delete_user_button + id)
    
    // Opdater styling
    delete_user_button_element.classList.remove("hidden")
    delete_user_button_element.classList.add("flex")
    
    show_confirm_buttons_admin_element.classList.remove("flex")
    show_confirm_buttons_admin_element.classList.add("hidden")
}

/**
 * Lav et request til vores api om at gøre brugeren aktiv igen
 */
async function activate_user() {
    try {
        // Hent event target som i vores tilfælde er en form
        const frm = event.target.form

        // Lav reqeust til vores API om at activate-user
        const conn = await fetch("/activate-user", {
            method : "POST",
            body : new FormData(frm),        
        })

        // Hent response fra API
        const data = await conn.json()

        // Tjek om requestet var succesfuldt
        if( !conn.ok || data.info != "ok" ) {
            throw new TypeError("Something went wrong. Cannot write comment to tweet");
        }

        // Reload siden
        location.reload()
    } 
    catch ({ name, message }) {
        console.log(name); 
        console.log(message); 
    }
}

/**
 * Lav et request til vores api om at slette brugeren fra databasen
 */
async function delete_user() {
    try {
        // Hent event target som i vores tilfælde er en form
        const frm = event.target.form

        // Lav reqeust til vores API om at activate-user
        const conn = await fetch("/delete-user", {
            method : "DELETE",
            body : new FormData(frm),        
        })

        // Hent response fra API
        const data = await conn.json()

        // Tjek om requestet var succesfuldt
        if( !conn.ok || data.info != "ok" ) {
            throw new TypeError("Something went wrong. Cannot write comment to tweet");
        }

        // Reload siden
        location.reload()
    } 
    catch ({ name, message }) {
        console.log(name); 
        console.log(message); 
    }
}

    

// Definer globale variabler
let active_popup = null;
let user_options_btn_g 
let user_option_popup
const cancel_delete_user_btn = document.getElementById("cancel_delete_user_btn")




/**
 * Hent og toggle popup user options til enten at være synlig eller usynlig
 * @param {HTMLElement} user_options_btn - Button element der ver klikket på for at aktivere denne funktion.
 */
function open_user_options(user_options_btn) {
    // Definer først del af user_option_popup_text elementes id
    const user_option_popup_text = "user_option_popup_";

    // Split input elements id for hvert "_" karakter, for at få id'et som står bagerst 
    const parts = user_options_btn.id.split("_");
    const id = parts[parts.length - 1];

    // Definer det fulde id på det element vi ønsker at finde og hent det
    const user_option_popup_and_id = user_option_popup_text + id;
    user_option_popup = document.getElementById(user_option_popup_and_id);
    
    // Skjul popup
    if (active_popup && active_popup.popup !== user_option_popup) {
        active_popup.popup.classList.remove("flex");
        active_popup.popup.classList.add("hidden");
        active_popup = null;
    }

    // Toggle popup elemented til enten at være synlig eller usynlig
    if (user_option_popup.classList.contains("hidden")) {
        user_option_popup.classList.remove("hidden");
        user_option_popup.classList.add("flex");
        active_popup = { button: user_options_btn, popup: user_option_popup };
    } else {
        user_option_popup.classList.remove("flex");
        user_option_popup.classList.add("hidden");
        active_popup = null;
    }
}

/**
 * Denne funktion bliver kaldt en gang når js filen bliver importeret
 * - Formålet med dette er at lave kun en eventlistener.
 */
function init() {
    // Opret event listner når brugeren klikker på musen
    document.addEventListener("click", (e) => {
        // Tjek om brugeren har klikket inden for knappen og popup vinduet: Hvis true så luk popup
        if (active_popup && e.target !== active_popup.button && !active_popup.popup.contains(e.target)  && !active_popup.button.contains(e.target) || e.target == cancel_delete_user_btn) {
            active_popup.popup.classList.remove("flex");
            active_popup.popup.classList.add("hidden");
            active_popup = null

            // Hvis Admin har klikket på "delete" knappen, men lukket pop-uppen ved at klikke på skærm i stedet for "cancel" knappen - det her stiller til default
            const show_confirm_buttons = document.getElementById("show_confirm_buttons")
            show_confirm_buttons.style.display = "none"
        } 
    });
}

// Kald init når js filen bliver importeret
init()
