import React from "react";
import {makeStyles} from "@material-ui/core/styles";
import {Paper, TableBody, TableCell, TableContainer, TableRow} from "@material-ui/core";
import TableHead from "@material-ui/core/TableHead";
import Table from "@material-ui/core/Table";


const useStyles = makeStyles(theme => ({
    table: {
        minWidth: 650,
    }
}));


export default function CreditCardBenefit() {
    const classes = useStyles();
    const rows = [
        {bank: 'BOA', name: 'cash reward', owner: 'weidong', reward: 'restaurant', xpoints: 3, start: '2020-3', end: 'null'},
        {bank: 'Chase', name: 'freedom', owner: 'weidong', reward: 'restaurant', xpoints: 3, start: '2020-3', end: 'null'},
        {bank: 'American Express', name: 'shopping card', owner: 'weidong', reward: 'restaurant', xpoints: 3, start: '2020-3', end: 'null'},
        {bank: 'Discover', name: 'cash reward', owner: 'weidong', reward: 'restaurant', xpoints: 3, start: '2020-3', end: 'null'},
    ];

    return (
        <TableContainer component={Paper}>
            <Table className={classes.table} aria-label="cc benfits">
                <TableHead>
                    <TableRow>
                        <TableCell>Reward</TableCell>
                        <TableCell>Name</TableCell>
                        <TableCell>Bank</TableCell>
                        <TableCell>Owner</TableCell>
                        <TableCell>XPoints</TableCell>
                        <TableCell>Start</TableCell>
                        <TableCell>End</TableCell>
                        <TableCell>Last4 Digits</TableCell>
                    </TableRow>
                </TableHead>
                <TableBody>
                    {rows.map((row, index) => (
                        <TableRow key={index}>
                            <TableCell>{row.reward}</TableCell>
                            <TableCell>{row.name}</TableCell>
                            <TableCell>{row.bank}</TableCell>
                            <TableCell>{row.owner}</TableCell>
                            <TableCell>{row.xpoints}</TableCell>
                            <TableCell>{row.start}</TableCell>
                            <TableCell>{row.end}</TableCell>
                        </TableRow>
                    ))}
                </TableBody>
            </Table>
        </TableContainer>
    );
}