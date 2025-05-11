export async function fetchApi(route: string, config: any = undefined) {
    return await fetch(`${import.meta.env.VITE_API_URL}${route}`, {
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        ...config
    })
}
