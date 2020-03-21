import React from "react";
import {makeStyles, withStyles} from "@material-ui/core/styles";
import {Paper, TableBody, TableCell, TableContainer, TableRow} from "@material-ui/core";
import TableHead from "@material-ui/core/TableHead";
import Table from "@material-ui/core/Table";


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
    const rows = [
        {bank: 'BOA', name: 'cash reward', owner: 'weidong', reward: 'restaurant', xpoints: 3, start: '2020-3', end: 'null', last4digits: 9999},
        {bank: 'Chase', name: 'freedom', owner: 'weidong', reward: 'restaurant', xpoints: 3, start: '2020-3', end: 'null', last4digits: 9999},
        {bank: 'American Express', name: 'shopping card', owner: 'weidong', reward: 'restaurant', xpoints: 3, start: '2020-3', end: 'null', last4digits: 9999},
        {bank: 'Discover', name: 'cash reward', owner: 'weidong', reward: 'restaurant', xpoints: 3, start: '2020-3', end: 'null', last4digits: 9999},
    ];

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
                    {rows.map((row, index) => (
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