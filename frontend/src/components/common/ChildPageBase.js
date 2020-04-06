import React from "react";
import {makeStyles} from "@material-ui/core/styles";
import {APP_BAR_HEIGHT} from "../utils/globalParams";
import grey from "@material-ui/core/colors/grey";
import Paper from "@material-ui/core/Paper";
import Container from "@material-ui/core/Container";


const useStyles = makeStyles(theme => ({
    root: {
        display: 'flex',
        flexWrap: 'wrap',
        height: `calc(100% - ${APP_BAR_HEIGHT}px)`,
    },
    container: {
        backgroundColor: grey[200],
    }
}));

export default function ChildPageBase({children, maxWidth="sm"}) {
    const classes = useStyles();
    return (
        <Paper className={classes.root}>
            <Container maxWidth={maxWidth} className={classes.container}>
                {children}
            </Container>
        </Paper>
    )
}