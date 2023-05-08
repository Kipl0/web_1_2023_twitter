
// Hide
function hide_search_reults() {
    document.querySelector("#search_results").classList.add("hidden")
    // search_results.style.display = "none"
}

// Show
function show_search_results() {
    document.querySelector("#search_results").classList.remove("hidden")
    // search_results.style.display = "flex"
  }
//   document.querySelector("#search_results").classList.add("hidden")

let the_timer
function search() {
    clearTimeout(the_timer)
    the_timer = setTimeout(async function() {
        const conn = await fetch("/search", {
            method : "POST"
        }) //second argument is a json object - fordi vi beder den returnere json
        const data = await conn.json()
        

        let results = ""
        
        document.querySelector("#search_results").innerHTML = ""
        data.forEach( (item)=>{
            results += `<div>${item.name}</div>`
        })
        console.log(results)
        document.querySelector("#search_results").insertAdjacentHTML('afterbegin',results)

    }, 500)
}
