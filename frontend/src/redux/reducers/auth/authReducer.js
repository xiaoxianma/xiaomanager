import {SET_USER_AUTH} from "../../actions/auth/authActionTypes";

const initialState = {
    auth: {
        username: "",
        isAuthenticated: true,
        token: "",
    }
};

export function userAuth(state = initialState.auth, action) {
    switch (action.type) {
        case SET_USER_AUTH:
            return action.userAuth;
        default:
            return state;
    }
}