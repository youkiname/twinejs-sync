import { fetchApi } from "../api-base";


type PassageId = string;

const activePassage: PassageId = ''
let intervalId: any = null


export function useServerTextSync(passageId: PassageId, callback: (newText: string) => void): () => void {
    if (activePassage === passageId || !passageId) return () => {
        if (intervalId !== null) {
            clearInterval(intervalId);
        }
    }
    if (intervalId !== null) {
        clearInterval(intervalId);
    }

    intervalId = setInterval(async () => {
        const res = await fetchApi(`/get/passage/${passageId}`)
        const passage = await res.json()
        callback(passage.text)
    }, 3000)
    return () => {
        if (intervalId !== null) {
            clearInterval(intervalId);
        }
    }
}
