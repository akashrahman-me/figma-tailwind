def convert_tailwind(data):
    # Formatting the data into the desired structure for the .ts file
    return f"""
    import type {{ Config }} from "tailwindcss";
    import {{fontFamily}} from "tailwindcss/defaultTheme";

    const config: Config = {{
        content: ["./index.html", "./src/**/*.{{js,ts,jsx,tsx}}"],
        theme: {{
            extend: {{
                colors: {data['colors']},
            }},
            fontSize: {data['fontSize']},
            boxShadow: {data['boxShadow']},
            fontFamily: {data['fontFamily']},
        }},
        plugins: [],
    }};

    export default config;
    """


