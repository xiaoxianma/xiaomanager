import React from "react";
import {makeStyles} from "@material-ui/core/styles";
import Button from "@material-ui/core/Button";
import CloudUploadOutlinedIcon from '@material-ui/icons/CloudUploadOutlined';
import {grey} from "@material-ui/core/colors";

const useStyles = makeStyles(theme => ({
    cloudBtn: {
        marginTop: theme.spacing(1),
        marginBottom: theme.spacing(1),
        backgroundColor: grey[100],
    },
}));

export default function MerchantImageUpload(props) {
    const classes = useStyles();

    return (
        <div>
            <input
                accept="image/*"
                type="file"
                onChange={props.handleMerchantImage}
                id="icon-button-file"
                style={{display: 'none'}}
            />
            <label htmlFor="icon-button-file">
                <Button component="span" className={classes.cloudBtn} variant="contained" size="large">
                    <CloudUploadOutlinedIcon fontSize="large"/>
                </Button>
            </label>
        </div>
    );
}