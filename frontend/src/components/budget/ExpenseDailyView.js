import React, {useEffect, useState} from "react";
import {axiosGet} from "../utils/axiosHelper";
import {useSelector} from "react-redux";
import {CartesianGrid, Line, LineChart, ResponsiveContainer, Tooltip, XAxis, YAxis} from "recharts";
import Card from "@material-ui/core/Card";
import CardHeader from "@material-ui/core/CardHeader";
import CardContent from "@material-ui/core/CardContent";
import {makeStyles} from "@material-ui/core/styles";
import cardHeaderColor from "@material-ui/core/colors/brown";
import {useHistory} from "react-router-dom";

const useStyles = makeStyles(theme => ({
    cardHeader: {
        color: cardHeaderColor[500],
    },
}));

export default function ExpenseDailyView() {
    const history = useHistory();
    const classes = useStyles();
    const [data, setData] = useState([]);
    const userAuth = useSelector(state => state.userAuth);


    useEffect(() => {
        axiosGet("/api/budgetmgr/expense-daily/", userAuth.token)
            .then(res => {
                setData(res.data);
            })
            .catch(err => {
                console.error(`Failed to fetch daily expense, ${err}`);
            })
    }, [userAuth.token]);

    const handleFormatter = (value, name, props) => {
        return [`$${value.toFixed(2)}`, "expense"];
    };

    const handleDotClick = (event) => {
        const date = event.payload.transaction_date;
        history.push(`/expense-overview?datefrom=${date}&dateto=${date}`);
    };

    return (
        <Card>
            <CardHeader title="Daily Expense" className={classes.cardHeader}/>
            <CardContent>
                <ResponsiveContainer width="100%" aspect={5.0}>
                    <LineChart data={data} margin={{top: 5, right: 5, left: 5, bottom: 5}}>
                        <XAxis dataKey="transaction_date"/>
                        <YAxis/>
                        <CartesianGrid strokeDasharray="3 3"/>
                        <Tooltip formatter={handleFormatter}/>
                        <Line type="monotone" dataKey="amount" stroke="#8884d8"
                              activeDot={{r: 8, onClick: handleDotClick}}/>
                    </LineChart>
                </ResponsiveContainer>
            </CardContent>
        </Card>
    );
}
