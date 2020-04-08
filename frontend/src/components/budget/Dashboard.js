import React from "react";
import ExpenseDailyView from "./ExpenseDailyView";
import ExpenseMonthlyView from "./ExpenseMonthlyView";


export default function DashBoard() {
    return (
        <div>
            <ExpenseDailyView/>
            <ExpenseMonthlyView/>
        </div>
    );
}