import { app } from "../../../scripts/app.js";
import { api } from "../../../scripts/api.js";

app.registerExtension({
    name: "Pollinations.Settings",
    async setup() {
        const id = "Pollinations.ApiKey";
        const defaultValue = "";

        // Add setting to the ComfyUI Settings Menu
        app.ui.settings.addSetting({
            id,
            name: "Pollinations API Key (BYOP)",
            type: "text",
            defaultValue,
            onChange: (value) => {
                // When the setting changes, send it to the Python server to save
                api.fetchApi("/pollinations/save_key", {
                    method: "POST",
                    body: JSON.stringify({ api_key: value }),
                    headers: { "Content-Type": "application/json" }
                });
            },
        });
    },
});