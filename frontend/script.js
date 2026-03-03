const API_URL = "https://primer-proyecto-98hw.onrender.com/";
const CONVERSACION_ID = 1;

async function cargarHistorial() {
    const response = await fetch(`${API_URL}/mensajes/conversacion/${CONVERSACION_ID}`);
    const data = await response.json();

/mensajes/conversacion/{}
    const chatBox = document.getElementById("chatBox");
    chatBox.innerHTML = "";

    data.forEach(m => {
        const div = document.createElement("div");
        div.className = "message";
        div.innerText = m.rol + ": " + m.contenido;
        chatBox.appendChild(div);
    });
}

async function enviarMensaje() {
    const input = document.getElementById("mensajeInput");
    const error = document.getElementById("errorMensaje");
    const mensaje = input.value.trim();

    if (!mensaje) {
        error.innerText = "No puedes enviar mensaje vacío";
        return;
    }

    error.innerText = "";

    await fetch(`${API_URL}/mensajes`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            conversacion_id: CONVERSACION_ID,
            contenido: mensaje,
            rol: "usuario"
        })
    });

    input.value = "";
    cargarHistorial();
}

cargarHistorial();