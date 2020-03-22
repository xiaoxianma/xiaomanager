
import axios from 'axios';

export function axiosGet(endPoint, token) {
    return axios.get(`${process.env.PUBLIC_URL}${endPoint}`, { headers: {"Authorization": `Bearer ${token}`}})
}

