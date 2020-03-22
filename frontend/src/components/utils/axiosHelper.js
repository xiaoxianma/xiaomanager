import axios from 'axios';
import {DOMAIN} from "./domain";


export function axiosGet(endPoint, token) {
    return axios.get(`${DOMAIN}${endPoint}`, { headers: {"Authorization": `Bearer ${token}`}})
}

