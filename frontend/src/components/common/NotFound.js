import React from 'react';
import {makeStyles} from "@material-ui/core/styles";
import Typography from "@material-ui/core/Typography";
import Grid from "@material-ui/core/Grid";


const useStyle = makeStyles(theme => ({
    root: {
        padding: theme.spacing.unit * 4
    },
    contentWrapper: {
        marginTop: '150px',
        textAlign: 'center'
    },
    image: {
        display: 'inline-block',
        marginTop: '50px',
        maxWidth: '100%',
        width: '554px'
    }
}));

export default function NotFound() {
    const classes = useStyle();

    return (
        <div className={classes.root}>
            <Grid container justify="center" spacing={32}>
                <Grid item lg={6} xs={12}>
                    <div className={classes.contentWrapper}>
                        <Typography variant="h1">
                            404: The page you are looking for isn’t here
                        </Typography>
                        <Typography variant="subtitle2">
                            You either tried some shady route or you came here by mistake.
                            Whichever it is, try using the navigation
                        </Typography>
                        <img
                            alt="Under development"
                            className={classes.image}
                            src="/static/not-found.svg"
                        />
                    </div>
                </Grid>
            </Grid>
        </div>
    );
};

