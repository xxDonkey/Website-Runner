const url = ''

const repos = [
    "Museum-Ticket-Generator"
]

function on_load()
{
    var sidenav = document.getElementById('sidenav')

    repos.forEach(repo => {
        var a = document.createElement('a')
        a.setAttribute('href', url + repo)
        a.innerHTML = repo.replaceAll('-', ' ')
        sidenav.appendChild(a)
    });
}

function open_sidenav()
{
    document.getElementById('sidenav').style.width = '350px';
}

function close_sidenav()    
{
    document.getElementById('sidenav').style.width = '0';
}