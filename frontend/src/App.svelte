<script>
<<<<<<< HEAD
    import Router from "svelte-spa-router"
    import Home from "./routes/Home.svelte"
    const routes = {
        '/': Home,
    }
</script>

<Router {routes}/>
=======
    let message;
    fetch("http://127.0.0.1:8000/hello").then((response) => { 
        response.json().then((json) => {
            message = json.message; 
    });
    }); 
</script>

<h1>{message}</h1>
>>>>>>> e0386be075e27750059fc84ad9f9fdc4df450f00
