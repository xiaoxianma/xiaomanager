import {SET_USER_AUTH} from "../../actions/auth/authActionTypes";
import {initialState} from "../initialState";


export function userAuth(state = initialState.auth, action) {
    switch (action.type) {
        case SET_USER_AUTH:
            return action.userAuth;
        default:
            return state;
    }
}