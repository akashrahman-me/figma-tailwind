import {IBM_Plex_Sans} from "next/font/google";

const ibmPlexSans = IBM_Plex_Sans({
   subsets: ["latin"],
   weight: ["400", "500", "600", "700"],
   variable: "--font-ibm_plex_sans",
});

const fonts = [ibmPlexSans];
