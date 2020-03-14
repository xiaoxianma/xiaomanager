import {combineReducers} from "redux";
import {userAuth} from "./auth/authReducer";

export default combineReducers({
    userAuth,
});

