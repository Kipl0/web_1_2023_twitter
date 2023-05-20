let the_timer
// Hide
function hide_search_reults() {
    clearTimeout(the_timer)
    the_timer = setTimeout(async function() {
        document.querySelector("#search_results").classList.add("hidden")
    }, 700)
}

// // Show
// function show_search_results() {
//     document.querySelector("#search_results").classList.remove("hidden")
//     // search_results.style.display = "flex"
//   }
// //   document.querySelector("#search_results").classList.add("hidden")


function search() {
    clearTimeout(the_timer)

    const frm = event.target.form

    the_timer = setTimeout(async function() {
        const conn = await fetch("/search", {
            method : "POST",
            body : new FormData(frm)
        }) //second argument is a json object - fordi vi beder den returnere json
        const data = await conn.json()
        
        let results = ""
        
        document.querySelector("#search_results").innerHTML = ""
        data.forEach( (item)=>{
            results += `<a href="/${item.user_username}" class="flex flex-col px-4 py-3 hover:bg-zinc-800">
                        <section class="flex items-center gap-6">
                            <img src="/avatar/${item.user_avatar}" alt="" class="w-10 rounded-full aspect-square">
                            <section >

                            <div>${item.user_first_name} ${item.user_last_name}</div>
                            <div class="text-zinc-500 text-sm">@${item.user_username}</div>              
                            </section>
                        </section>
                        </a>`
        })
        
        document.querySelector("#search_results").insertAdjacentHTML('afterbegin',results)

        document.querySelector("#search_results").classList.remove("hidden")
        document.querySelector("#search_results").classList.add("flex")
    }, 500)
}
