import {SET_USER_AUTH} from "./authActionTypes";

export const setUserAuth = (userAuth) => {
    return {
        type: SET_USER_AUTH,
        userAuth
    };
};
