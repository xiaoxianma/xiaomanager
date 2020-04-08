import React from "react";
import {makeStyles} from "@material-ui/core/styles";
import {APP_BAR_HEIGHT} from "../utils/globalParams";
import grey from "@material-ui/core/colors/grey";
import Container from "@material-ui/core/Container";


const useStyles = makeStyles(theme => ({
    fixRoot: {
        display: 'flex',
        flexWrap: 'wrap',
        height: `calc(100% - ${APP_BAR_HEIGHT}px)`,
    },
    flexibleRoot: {
        display: 'flex',
        flexWrap: 'wrap',
        backgroundColor: grey[200],
    },
    container: {
        backgroundColor: grey[200],
    }
}));

export default function ChildPageBase({children, maxWidth="sm", flexibleHeight=true}) {
    const classes = useStyles();
    return (
        <div className={flexibleHeight ? classes.flexibleRoot : classes.fixRoot}>
            <Container maxWidth={maxWidth} className={classes.container}>
                {children}
            </Container>
        </div>
    )
}