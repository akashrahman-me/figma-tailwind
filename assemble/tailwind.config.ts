
    import type { Config } from "tailwindcss";
    import {fontFamily} from "tailwindcss/defaultTheme";

    const config: Config = {
        content: ["./index.html", "./src/**/*.{js,ts,jsx,tsx}"],
        theme: {
            extend: {
                colors: {'slate': {'500': '#737373'}, 'gray': {'50': '#ffffff', '600': '#4D5761', '900': '#0F172A'}, 'neutral': {'400': '#9DA4AE', '700': '#384250', '600': '#334155', '800': '#1F2A37', '900': '#161616'}, 'emerald': {'800': '#085D3A'}},
            },
            fontSize: {'xs': ['12px', {'lineHeight': '1.5em'}], 'sm': ['14px', {'lineHeight': '1.43em'}], 'md': ['16px', {'lineHeight': '1.5em'}], 'base': ['18px', {'lineHeight': '1.56em'}], 'lg': ['21px', {'lineHeight': '0.81em'}], 'xl': ['36px', {'lineHeight': '1.67em'}], '3xl': ['48px', {'lineHeight': '1.25em'}]},
            boxShadow: {'sm': '0px 1px 2px rgba(16, 24, 40, 0.05)'},
            fontFamily: {'ibm-plex-sans': ['var(--ibm-plex-sans)', "'...fontFamily.sans'"], 'akashrahman': ['var(--akashrahman)', "'...fontFamily.sans'"], 'rakib-islam': ['var(--rakib-islam)', "'...fontFamily.sans'"]},
        },
        plugins: [],
    };

    export default config;
    