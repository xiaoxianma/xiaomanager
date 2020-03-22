import axios from 'axios';
import {DOMAIN} from "./domain";


export function axiosGet(endpoint, token) {
    return axios.get(`${DOMAIN}${endpoint}`, { headers: {"Authorization": `Bearer ${token}`}});
}


export function axiosPost(endpoint, payload) {
    return axios.post(`${DOMAIN}${endpoint}`, payload);
}