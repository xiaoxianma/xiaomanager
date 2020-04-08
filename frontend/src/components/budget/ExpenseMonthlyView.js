import React, {useEffect, useState} from "react";
import {axiosGet} from "../utils/axiosHelper";
import {useSelector} from "react-redux";
import {Bar, BarChart, CartesianGrid, ResponsiveContainer, Tooltip, XAxis, YAxis} from "recharts";
import Card from "@material-ui/core/Card";
import CardHeader from "@material-ui/core/CardHeader";
import CardContent from "@material-ui/core/CardContent";
import {makeStyles} from "@material-ui/core/styles";
import cardHeaderColor from "@material-ui/core/colors/brown";
import brown from "@material-ui/core/colors/brown";
import pink from "@material-ui/core/colors/pink";
import purple from "@material-ui/core/colors/purple";
import indigo from "@material-ui/core/colors/indigo";
import blue from "@material-ui/core/colors/blue";
import cyan from "@material-ui/core/colors/cyan";
import teal from "@material-ui/core/colors/teal";
import green from "@material-ui/core/colors/green";
import yellow from "@material-ui/core/colors/yellow";
import amber from "@material-ui/core/colors/amber";
import lightGreen from "@material-ui/core/colors/lightGreen";

const CATEGORY_COLOR_MAP = {
    "Auto & Transport": pink[200],
    "Bills & Utilities": indigo[200],
    "Business Services": blue[200],
    "Education": purple[200],
    "Entertainment": cyan[400],
    "Fees & Charges": indigo[500],
    "Financial": blue[500],
    "Food & Dining": green[200],
    "Gifts & Donations": pink[500],
    "Grocery Stores": brown[300],
    "Health & Fitness": yellow[400],
    "Home": teal[200],
    "Income": indigo[800],
    "Kids": green[800],
    "Misc Expenses": pink[800],
    "Personal Care": blue[800],
    "Pets": teal[800],
    "Shopping": amber[500],
    "Taxes": purple[800],
    "Transfer": cyan[800],
    "Travel": lightGreen["A400"],
};

const useStyles = makeStyles(theme => ({
    cardHeader: {
        color: cardHeaderColor[500],
    },
}));

export default function ExpenseMonthlyView() {
    const classes = useStyles();
    const [data, setData] = useState([]);
    const userAuth = useSelector(state => state.userAuth);


    useEffect(() => {
        axiosGet("/api/budgetmgr/expense-monthly/", userAuth.token)
            .then(res => {
                buildData(res.data);
            })
            .catch(err => {
                console.error(`Failed to fetch monthly expense, ${err}`);
            })
    }, [userAuth.token]);

    const buildData = data => {
        const ret = [];
        for (let [key, values] of Object.entries(data)) {
            const entry = {date: key};
            for (const value of values) {
                entry[value.category] = value.amount;
            }
            ret.push(entry);
        }
        setData(ret);
    };

    const handleFormatter = (value, name, props) => {
        return [`$${value.toFixed(2)}`, name];
    };

    return (
        <Card>
            <CardHeader title="Monthly Expense" className={classes.cardHeader}/>
            <CardContent>
                <ResponsiveContainer width="100%" aspect={4.0}>
                    <BarChart data={data} margin={{top: 5, right: 5, left: 5, bottom: 5}}>
                        <XAxis dataKey="date"/>
                        <YAxis/>
                        <CartesianGrid strokeDasharray="3 3"/>
                        <Tooltip itemSorter={()=> 1} formatter={handleFormatter}/>
                        {
                            Object.entries(CATEGORY_COLOR_MAP).map(([category, color], index) => {
                                return <Bar key={index} dataKey={category} stackId="a" fill={color}/>;
                            })
                        }
                    </BarChart>
                </ResponsiveContainer>
            </CardContent>
        </Card>
    );
}