/** @odoo-module **/
import { Component, useState, App, xml, markup } from "@odoo/owl";

function escapeHtml(text) {
    return String(text)
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;");
}

function formatFecha() {
    return new Date().toLocaleString("es-EC", {
        day: "2-digit",
        month: "short",
        hour: "2-digit",
        minute: "2-digit",
        hour12: true,
    });
}

// ── OWL Component: lista de notas en memoria (se borra al recargar) ──
class NotasList extends Component {
    static template = xml`
        <div class="ob-notas-list">
            <t t-if="state.notas.length === 0">
                <div class="ob-chatter__empty">Sin notas en esta sesión</div>
            </t>
            <t t-foreach="state.notas" t-as="nota" t-key="nota.id">
                <div class="ob-msg">
                    <div class="ob-msg__avatar" t-esc="nota.iniciales"/>
                    <div class="ob-msg__content">
                        <div class="ob-msg__meta">
                            <span class="ob-msg__author" t-esc="nota.nombre"/>
                            <span t-esc="nota.fecha"/>
                        </div>
                        <div class="ob-msg__body" t-out="nota.cuerpo"/>
                    </div>
                </div>
            </t>
        </div>
    `;

    setup() {
        const notasFijas = [
            {
                id: 1,
                nombre: "Carlos Mendoza",
                iniciales: "CM",
                cuerpo: markup("<p>Necesitamos automatizar los flujos de ventas y facturación en Odoo 19. Vi que trabajas con n8n también, perfecto para lo que tenemos en mente. 🙌</p>"),
                fecha: "15-mar, 10:24 a. m.",
            },
        ];
        this.state = useState({ notas: notasFijas });

        window.addEventListener("pf-nota-nueva", (e) => {
            const { nombre, texto } = e.detail;
            const name = nombre.trim() || "Visitante";
            const htmlBody =
                "<p>" +
                escapeHtml(texto).replace(/\n/g, "<br/>") +
                "</p>";
            const nota = {
                id: Date.now(),
                nombre: name,
                iniciales: name.substring(0, 2).toUpperCase(),
                cuerpo: markup(htmlBody),
                fecha: formatFecha(),
            };
            this.state.notas = [nota, ...this.state.notas.filter(n => n.id !== 1), ...this.state.notas.filter(n => n.id === 1)];
        });
    }
}

function init() {
    const root = document.getElementById("ob-notas-root");
    if (root) {
        new App(NotasList).mount(root);
    }
}

if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
} else {
    init();
}
