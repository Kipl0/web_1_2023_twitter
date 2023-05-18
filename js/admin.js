


async function deactivate_user() {
    console.log("deactivate user");
    const frm = event.target.form
    const conn = await fetch("/deactivate-user", {
        method : "POST",
        body : new FormData(frm),        
    })
    const data = await conn.json()

    if( conn.ok && data.info == "ok" ) {
        console.log("deactivating user")
        location.reload()
    } else {
        console.log("cannot deactivate user")
    }

}

async function activate_user() {
    console.log("activate user");
    const frm = event.target.form
    const conn = await fetch("/activate-user", {
        method : "POST",
        body : new FormData(frm),        
    })
    const data = await conn.json()

    if( conn.ok && data.info == "ok" ) {
        console.log("activating user")
        location.reload()
    } else {
        console.log("cannot activate user")
    }
}


async function delete_user() {
    console.log("delete");
    const frm = event.target.form
    const conn = await fetch("/delete-user", {
        method : "DELETE",
        body : new FormData(frm),        
    })
    const data = await conn.json()

    if( conn.ok && data.info == "ok" ) {
        console.log("deleting user")
        location.reload()
    } else {
        console.log("cannot delete user")
    }
}






let active_popup = null;

let user_options_btn_g 
let user_option_popup

// lav kun en eventlistener ved init, og ikke ved hvert klik
function init() {
    // Close popup when clicked outside button and popup
    document.addEventListener("click", (e) => {
         if (active_popup && e.target !== active_popup.button && !active_popup.popup.contains(e.target)  && !active_popup.button.contains(e.target)) {
            active_popup.popup.classList.remove("flex");
            active_popup.popup.classList.add("hidden");
            active_popup = null
        } 
    });
}
init()

function open_user_options(user_options_btn) {
    user_options_btn_g = user_options_btn
    const user_option_popup_text = "user_option_popup_";

    // Split the text from the id where _
    const parts = user_options_btn.id.split("_");
    const id = parts[parts.length - 1];

    const user_option_popup_and_id = user_option_popup_text + id;

    user_option_popup = document.getElementById(user_option_popup_and_id);
    
    // Show and hide popup
    if (active_popup && active_popup.popup !== user_option_popup) {
        active_popup.popup.classList.remove("flex");
        active_popup.popup.classList.add("hidden");
        active_popup = null;
    }

    // Toggle the visibility of the popup
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
