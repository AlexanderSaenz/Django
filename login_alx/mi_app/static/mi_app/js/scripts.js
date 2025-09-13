document.addEventListener("DOMContentLoaded", () => {

    // Loader (solo index.html)
    if (document.querySelector("#loader") && document.querySelector("#content")) {
        gsap.fromTo("circle", 
            { strokeDashoffset: 283 },  
            { strokeDashoffset: 0, duration: 2, repeat: -1, ease: "linear" }
        );

        setTimeout(() => {
            gsap.to("#loader", { opacity: 0, duration: 1, onComplete: () => {
                document.getElementById("loader").style.display = "none";
            }});
            
            gsap.to("#content", { opacity: 1, duration: 1, delay: 0.5 });

            gsap.to(".intro", {
                opacity: 1,
                y: 0,
                duration: 1,
                delay: 1
            });
        }, 3000);
    }

    // Botón dark/light (solo index.html)
    const btn = document.getElementById("toggle-theme");
    if (btn) {
        btn.addEventListener("click", () => {
            document.body.classList.toggle("light-mode");
            btn.textContent = document.body.classList.contains("light-mode") ? "☀️" : "🌙";
            localStorage.setItem("theme", document.body.classList.contains("light-mode") ? "light" : "dark");
        });

        window.addEventListener("load", () => {
            const theme = localStorage.getItem("theme");
            if (theme === "light") {
                document.body.classList.add("light-mode");
                btn.textContent = "☀️";
            }
        });
    }

    // Animación de tarjetas (solo portafolio.html)
    if (document.querySelector(".card")) {
        gsap.to(".card", {
            opacity: 1,
            y: 0,
            duration: 1,
            stagger: 0.3,
            ease: "power3.out"
        });
    }
});
