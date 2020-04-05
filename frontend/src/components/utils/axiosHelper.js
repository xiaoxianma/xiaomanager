import axios from 'axios';
import {DOMAIN} from "./domain";


export function axiosGet(endpoint, token) {
    return axios.get(`${DOMAIN}${endpoint}`, { headers: {"Authorization": `Bearer ${token}`}});
}


export function axiosPost(endpoint, payload, token=null) {
    if (token) {
        return axios.post(`${DOMAIN}${endpoint}`, payload, {headers: {"Authorization": `Bearer ${token}`}});
    } else {
        return axios.post(`${DOMAIN}${endpoint}`, payload);
    }
}