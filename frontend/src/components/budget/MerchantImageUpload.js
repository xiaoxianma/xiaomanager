import React from "react";
import {makeStyles} from "@material-ui/core/styles";
import Button from "@material-ui/core/Button";
import CloudUploadOutlinedIcon from '@material-ui/icons/CloudUploadOutlined';
import {axiosPut} from "../utils/axiosHelper";
import {useSelector} from "react-redux";
import {grey} from "@material-ui/core/colors";

const useStyles = makeStyles(theme => ({
    button: {
        marginTop: theme.spacing(1),
        marginBottom: theme.spacing(1),
        backgroundColor: grey[100],
    },
}));

export default function MerchantImageUpload() {
    const classes = useStyles();
    const userAuth = useSelector(state => state.userAuth);

    const handleOnChange = (event) => {
        const file = event.target.files[0];
        const data = new FormData();
        data.append("file", file);
        axiosPut(`/api/budgetmgr/merchant-image-upload/`, data, userAuth.token)
            .then(res => {
                console.log("upload image successfully")
            })
            .catch(err => {
                console.error(`Failed to upload image, ${err}`);
            })
    };

    return (
        <div>
            <input
                accept="image/*"
                type="file"
                onChange={handleOnChange}
                id="icon-button-file"
                style={{display: 'none'}}
            />
            <label htmlFor="icon-button-file">
                <Button
                    component="span"
                    className={classes.button}
                    variant="contained"
                    size="large"
                >
                    <CloudUploadOutlinedIcon fontSize="large"/>
                </Button>
            </label>
        </div>
    );
}