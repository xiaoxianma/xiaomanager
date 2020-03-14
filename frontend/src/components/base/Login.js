import React, {useState, useEffect} from "react";
import axios from "axios";
import {useHistory} from "react-router-dom";
import TextField from "@material-ui/core/TextField";
import {makeStyles} from "@material-ui/core/styles";
import Card from "@material-ui/core/Card";
import CardActions from "@material-ui/core/CardActions";
import Button from "@material-ui/core/Button";
import CardHeader from "@material-ui/core/CardHeader";
import CardContent from "@material-ui/core/CardContent";
import {useDispatch, useSelector} from "react-redux";
import {setUserAuth} from "../../redux/actions/auth/authActions";

const useStyle = makeStyles(theme => ({
    container: {
        display: 'flex',
        flexWrap: 'wrap',
        width: 400,
        margin: `${theme.spacing(0)} auto`
    },
    loginBtn: {
        marginTop: theme.spacing(2),
        flexGrow: 1
    },
    header: {
        textAlign: 'center',
        background: '#212121',
        color: '#fff'
    },
    card: {
        marginTop: theme.spacing(10)
    }
}));

export default function Login() {
    const userAuth = useSelector(state => state.userAuth);
    const dispatch = useDispatch();
    const classes = useStyle();
    const history = useHistory();
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [isButtonDisabled, setIsButtonDisabled] = useState(true);
    const [helperText, setHelperText] = useState('');
    const [error, setError] = useState(false);

    useEffect(() => {
        if (username.trim() && password.trim()) {
            setIsButtonDisabled(false);
        } else {
            setIsButtonDisabled(true);
        }
    }, [username, password]);

    useEffect(() => {
        if (!userAuth.username) return;
        if (userAuth.isAuthenticated) {
            console.log(`${userAuth.username} login successfully`);
            setError(false);
            setHelperText(`Welcome back ${userAuth.username}`);
            history.push('/');
        } else {
            console.log(`${userAuth.username} login failed`);
            setError(true);
            setHelperText('Incorrect username or password');
        }
        // eslint-disable-next-line
    }, [userAuth]);

    const handleLogin = () => {
        axios.post(`${process.env.PUBLIC_URL}/api/token`, {username, password})
            .then(res => {
                dispatch(setUserAuth({username, isAuthenticated: true, token: res.access}));
            })
            .catch(err => {
                console.error(`Failed to authenticate ${username} | ${err}`);
            });
    };

    const handleKeyPress = e => {
        if (e.KeyCode === 13 || e.which === 13) {
            isButtonDisabled || handleLogin();
        }
    };

    return (
        <form className={classes.container} noValidate autoComplete="off">
            <Card className={classes.card}>
                <CardHeader className={classes.header} title="Login" />
                <CardContent>
                    <div>
                        <TextField
                            error={error}
                            fullWidth
                            id="username"
                            type="email"
                            label="Username"
                            placeholder="Username"
                            margin="normal"
                            onChange={(e)=>setUsername(e.target.value)}
                            onKeyPress={(e)=>handleKeyPress(e)}
                        />
                        <TextField
                            error={error}
                            fullWidth
                            id="password"
                            type="password"
                            label="Password"
                            placeholder="Password"
                            margin="normal"
                            helperText={helperText}
                            onChange={(e)=>setPassword(e.target.value)}
                            onKeyPress={(e)=>handleKeyPress(e)}
                        />
                    </div>
                </CardContent>
                <CardActions>
                    <Button
                        variant="contained"
                        size="large"
                        color="secondary"
                        className={classes.loginBtn}
                        onClick={()=>handleLogin()}
                        disabled={isButtonDisabled}>
                        Login
                    </Button>
                </CardActions>
            </Card>
        </form>
    );
}
