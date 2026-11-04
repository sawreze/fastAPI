<script>
    import {link} from 'svelte-svelte-spa-router'
</script>
<nav class="navber navber-expand-lg navber-light bg-light border-bottom">
    <div class="container-fluid" href="/">
        <a use:link class="navbar-brand" href="/">Pyto</a>
        <button
            class="navber-toggler"
            type="button"
            data-bs-toggle="collapse"
            data-bs-target="#navbarSupportedContent"
            aria-controls="#navberSupportedContent"
            aria-expanded="false"
            aria-label="Toggle navigation">
        <span class="navbar-toggle-icon"></span>
        </button>
        <div class="collase navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                <li class="nav-item">
                    <a use:link href="/user-create" class="nav-link">회원가입</a>
                </li>
                <li class="nav-item">
                    <a use:link class="nav-link" href="/user-login">로그인</a>
                </li>
            </ul>
        </div>
    </div>
</nav>