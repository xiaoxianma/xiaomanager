import React, {useEffect, useState} from "react";
import {makeStyles, withStyles} from "@material-ui/core/styles";
import {Paper, TableBody, TableCell, TableContainer, TableRow} from "@material-ui/core";
import TableHead from "@material-ui/core/TableHead";
import Table from "@material-ui/core/Table";
import axios from "axios";
import {useSelector} from "react-redux";
import {axiosGet} from "../../utils/axiosHelper";


const useStyles = makeStyles(theme => ({
    table: {
        minWidth: 650,
    }
}));


const StyledTableCell = withStyles(theme => ({
    head: {
        backgroundColor: theme.palette.common.black,
        color: theme.palette.common.white,
    },
    body: {
        fontSize: 14,
    }
}))(TableCell);


export default function CreditCardBenefit() {
    const classes = useStyles();
    const userAuth = useSelector(state => state.userAuth);
    const [benefits, setBenefits] = useState([]);

    useEffect(() => {
        axiosGet("/api/budgetmgr/current-rewards/", userAuth.token)
            .then(res => {
                buildBenefitsData(res);
            }).catch(err => {
                console.error("Failed to fetch current rewards");
            });
    }, []);

    const buildBenefitsData = data => {
        const ret = [];
        // eslint-disable-next-line array-callback-return
        data.map(row => {
            ret.push({
                bank: row.account.institution.name,
                name: row.account.alias,
                owner: row.account.owner.name,
                reward: row.reward_type.name,
                xpoints: row.xpoints,
                start: row.start_time,
                end: row.end_time,
                last4digits: row.acc.number.slice(-4),
            })
        });
        setBenefits(ret);
    };

    return (
        <TableContainer component={Paper}>
            <Table className={classes.table} aria-label="cc benfits">
                <TableHead>
                    <TableRow>
                        <StyledTableCell>Reward</StyledTableCell>
                        <StyledTableCell>Name</StyledTableCell>
                        <StyledTableCell>Bank</StyledTableCell>
                        <StyledTableCell>Owner</StyledTableCell>
                        <StyledTableCell>XPoints</StyledTableCell>
                        <StyledTableCell>Start</StyledTableCell>
                        <StyledTableCell>End</StyledTableCell>
                        <StyledTableCell>Last4 Digits</StyledTableCell>
                    </TableRow>
                </TableHead>
                <TableBody>
                    {benefits.map((row, index) => (
                        <TableRow key={index}>
                            <StyledTableCell>{row.reward}</StyledTableCell>
                            <StyledTableCell>{row.name}</StyledTableCell>
                            <StyledTableCell>{row.bank}</StyledTableCell>
                            <StyledTableCell>{row.owner}</StyledTableCell>
                            <StyledTableCell>{row.xpoints}</StyledTableCell>
                            <StyledTableCell>{row.start}</StyledTableCell>
                            <StyledTableCell>{row.end}</StyledTableCell>
                            <StyledTableCell>{row.last4digits}</StyledTableCell>
                        </TableRow>
                    ))}
                </TableBody>
            </Table>
        </TableContainer>
    );
}